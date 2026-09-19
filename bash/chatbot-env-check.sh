#!/usr/bin/env bash
set -u

echo "Chatbot environment check"
echo "========================="
printf "Host: "; hostname
printf "OS: "; uname -srm

for cmd in python3 node npm php curl jq; do
  if command -v "$cmd" >/dev/null 2>&1; then
    printf "%-10s OK\n" "$cmd"
  else
    printf "%-10s MISSING\n" "$cmd"
  fi
done
