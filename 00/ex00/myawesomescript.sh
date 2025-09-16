#!/bin/sh

[ $# -eq 0 ] && echo "Usage: $0 <url>" && exit 1

case "$1" in bit.ly/*) ;; *) echo "Error: URL must start with bit.ly/" && exit 1 ;; esac

result=$(curl -s --connect-timeout 5 --max-time 10 -w "%{url_effective}|%{http_code}" -o /dev/null "$1")
url=$(echo "$result" | cut -d'|' -f1)
code=$(echo "$result" | cut -d'|' -f2)

[ "$code" = "000" ] && echo "Error: Connection failed" && exit 1
echo "$code" | grep -q "^[45]" && echo "Error: HTTP $code" && exit 1

echo "$url"