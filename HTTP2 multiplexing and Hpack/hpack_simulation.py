"""
HPACK HEADER COMPRESSION

Problem:
---------

Request 1

Authorization: Bearer xyz
User-Agent: Chrome
Accept: application/json

Request 2

Authorization: Bearer xyz
User-Agent: Chrome
Accept: application/json

HTTP/1.1 sends the same strings repeatedly.

HPACK stores headers in a table.

Index 1 -> Authorization: Bearer xyz
Index 2 -> User-Agent: Chrome
Index 3 -> Accept: application/json

Future requests send:

1
2
3

instead of full strings.
"""


class HPACKEncoder:
    def __init__(self):
        self.dynamic_table = {}
        self.next_index = 1

    def encode(self, headers):

        encoded = []

        for header in headers:
            if header in self.dynamic_table:
                encoded.append(("INDEX", self.dynamic_table[header]))

            else:
                idx = self.next_index

                self.dynamic_table[header] = idx

                self.next_index += 1

                encoded.append(("LITERAL", header))

        return encoded


encoder = HPACKEncoder()

request1 = [
    "Authorization: Bearer xyz",
    "User-Agent: Chrome",
    "Accept: application/json",
]

request2 = [
    "Authorization: Bearer xyz",
    "User-Agent: Chrome",
    "Accept: application/json",
]

print("Request 1")
print(encoder.encode(request1))

print("\nRequest 2")
print(encoder.encode(request2))
