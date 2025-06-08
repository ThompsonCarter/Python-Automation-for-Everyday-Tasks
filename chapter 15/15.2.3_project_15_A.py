# Fix a Silent Bug
# Script divides by stock count; crash on zero.

# Add breakpoint() inside loop—inspect count values.
# Patch with if count == 0: continue.
