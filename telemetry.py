from lightnode import LightNode
from time import sleep

node = LightNode(34, 25, 14800, 47000)
while True:
    print(f"light={node.read_pct():.1f}")
    sleep(1)