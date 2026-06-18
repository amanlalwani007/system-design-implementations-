# HTTP/2 Core Improvements
#
# 1. Multiplexing
#    - Multiple streams share one TCP connection.
#    - Data is split into frames.
#    - Frames are interleaved on the wire.
#    - Stream IDs allow reconstruction.
#
# 2. HPACK
#    - Compresses HTTP headers.
#    - Uses static and dynamic header tables.
#    - Repeated headers become indexes.
#
# Benefits:
#    - Fewer TCP connections
#    - Reduced latency
#    - Reduced bandwidth
#    - Better network utilization
#
# Limitation:
#    - Still uses a single TCP connection.
#    - Packet loss blocks all streams at TCP level.
#    - This TCP Head-of-Line blocking led to HTTP/3 + QUIC.


"""
HTTP/2 MULTIPLEXING DEMO

HTTP/1.1
---------
Connection:
    Request A
    Response A

    Request B
    Response B

Responses are effectively serialized.

HTTP/2
-------
One TCP Connection

Stream 1 -> HTML
Stream 3 -> CSS
Stream 5 -> JS

Frames from different streams can be interleaved.

Frame(Stream=1)
Frame(Stream=3)
Frame(Stream=5)
Frame(Stream=1)
Frame(Stream=3)

Receiver reconstructs responses using Stream IDs.
"""

from dataclasses import dataclass


@dataclass
class Frame:
    stream_id: int
    data: str


connection_frames = []

# HTML response
connection_frames.append(Frame(1, "<html>"))

# CSS response
connection_frames.append(Frame(3, "body{"))

# JS response
connection_frames.append(Frame(5, "console"))

# Continue HTML
connection_frames.append(Frame(1, "</html>"))

# Continue CSS
connection_frames.append(Frame(3, "}"))

streams = {}

for frame in connection_frames:
    streams.setdefault(frame.stream_id, [])

    streams[frame.stream_id].append(frame.data)

print("Reconstructed Streams")

for stream_id, chunks in streams.items():
    print(f"Stream {stream_id}:", "".join(chunks))
