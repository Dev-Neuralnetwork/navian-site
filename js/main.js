/* Navian Digital — sticky masthead, mobile menu, scroll reveals. */

(function () {
  'use strict';

  var mast = document.getElementById('masthead');
  if (mast) {
    var top = document.querySelector('.topbar');
    var trigger = top ? top.offsetHeight : 8;
    var onScroll = function () {
      mast.classList.toggle('is-stuck', window.scrollY > trigger);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  var burger = document.getElementById('burger');
  var nav = document.getElementById('mobileNav');
  if (burger && nav) {
    var setOpen = function (open) {
      nav.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
    };
    burger.addEventListener('click', function () {
      setOpen(burger.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setOpen(false);
    });
  }

  /* --- parallax backgrounds ------------------------------------------- */
  var slow = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var layers = Array.prototype.slice.call(document.querySelectorAll('.band__bg'));

  if (layers.length && !slow) {
    var depth = 0.16;
    var ticking = false;

    var place = function () {
      var vh = window.innerHeight;
      layers.forEach(function (el) {
        var band = el.parentElement.getBoundingClientRect();
        if (band.bottom < 0 || band.top > vh) return;
        var mid = band.top + band.height / 2 - vh / 2;
        el.style.transform = 'translate3d(0,' + (-mid * depth).toFixed(1) + 'px,0)';
      });
      ticking = false;
    };

    var request = function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(place);
    };

    place();
    window.addEventListener('scroll', request, { passive: true });
    window.addEventListener('resize', request);
  }

  if (!('IntersectionObserver' in window)) return;

  var targets = document.querySelectorAll(
    '.band__content > h1, .band__content > h2, .keyart, .lede, .framed, .btn-row, .entry'
  );

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      io.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -6% 0px', threshold: 0.05 });

  targets.forEach(function (el, i) {
    el.classList.add('reveal');
    el.style.transitionDelay = (i % 3) * 90 + 'ms';
    io.observe(el);
  });
})();
