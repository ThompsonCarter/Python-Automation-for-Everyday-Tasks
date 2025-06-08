
python - <<'EOF'
from phue import Bridge
Bridge('192.168.1.50').set_light([1,2], 'on', True)
EOF
