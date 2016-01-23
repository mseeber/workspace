#!/bin/bash

glyph_play=">"
glyph_pause="||"

glyph_sun="☀"
glyph_moon="☽"

glyph_bat=" ▂ ▃ ▄ ▅ ▆ ▇ █"

datetime() {
    echo -ne $(date '+%F %H:%M')
}

songinfo() {
    echo -ne $(mocp -Q '%song - %album' 2> /dev/null)
}

battery() {
    echo -ne $(acpi | cut -d\  -f4-4 | sed 's/,//' | tr '\n' ' ')
}

moc_status() {
    STATUS="$(mocp -i 2> /dev/null | cut -d' ' -f2- | head -n1 )"
    if [ "$STATUS" = "PLAY" ]; then 
        STATUS_STR="[${glyph_play}] $(songinfo)"
    elif [ "$STATUS" = "PAUSE" ]; then
        STATUS_STR="[${glyph_pause}] $(songinfo)"
    else
        STATUS_STR="[MUSIC OFF]"
    fi

    echo -ne "$STATUS_STR"
}

update_cycle() {
    xsetroot -name "$(moc_status) [bat: $(battery)] $(datetime)"
}

update_cycle
