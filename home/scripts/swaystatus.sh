#!/usr/bin/env sh

glyph_ethernet='🖧 '
glyph_wifi='📶'

clock() {
    echo -ne $(date +'%Y-%m-%d %H:%M')
}

battery() {
    echo -ne $(acpi | cut -d\  -f4-4 | sed 's/,//' | tr '\n' ' ')
}

network() {
    connection_type=$(nmcli connection show --active | sed -e 1d | cut -d\  -f5)
    if [ 'wifi' =  "$connection_type" ];
    then
        echo -ne $glyph_wifi
    fi
}

while true; do
    echo -ne "[$(network)] [🔋 $(battery)] $(clock)"
    sleep 10
done
