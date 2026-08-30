#!/usr/bin/env bash
# Rebuild the site's JPEGs from their original Steam-asset PNGs.
#
# The pix_fmt is the point of this script. ffmpeg's mjpeg encoder picks 4:4:4
# chroma for RGB input, and iOS Safari's JPEG decoder is unreliable with 4:4:4 —
# affected images simply fail to paint, with no console error. Forcing
# yuvj420p is what makes them load on iPhone.
#
# Always encode from the PNG sources, never from the existing JPEGs, or each
# run compounds generation loss.
#
#   bash tools/build_images.sh
set -euo pipefail

SITE="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$SITE/assets/img"
STEAM="D:/My games/my-game/steam/steam_requirements_v1"
SHOTS="D:/My games/_offering_current/steam/screenshots"

jpg() { # src dst scale-filter quality
  ffmpeg -loglevel error -y -i "$1" ${3:+-vf "$3"} -pix_fmt yuvj420p -q:v "$4" "$2"
}

jpg "$STEAM/library_hero_3840x1240.png"        "$OUT/hero_bg.jpg"            "scale=2400:-2" 4
jpg "$STEAM/store_header_920x430.png"          "$OUT/offering_capsule.jpg"   ""              3
jpg "$STEAM/store_vertical_748x896.png"        "$OUT/offering_vertical.jpg"  ""              3
jpg "$STEAM/optional_page_background_1438x810.jpg" "$OUT/page_bg.jpg"        ""              4

for s in 1_early_day 2_night_wave 3_night_boss 4_late_day 5_late_night; do
  jpg "$SHOTS/$s.png" "$OUT/shot_$s.jpg" "scale=1280:-2" 4
done

printf '\n%-26s %s\n' "FILE" "CODEC,W,H,PIX_FMT"
for f in "$OUT"/*.jpg; do
  printf '%-26s ' "$(basename "$f")"
  ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,pix_fmt -of csv=p=0 "$f"
done
