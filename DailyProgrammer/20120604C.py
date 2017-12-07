"""
The basic idea of RSA starts with two large prime numbers of equal bit-length, p and q; their product n becomes the
modulus of the cryptosystem. The totient of n is computed as φ(pq) = (p−1) × (q−1). Then two keys are chosen, the
encryption key e and the decryption key d, such that de ≡ 1 (mod φ(pq)) and gcd(e, φ(pq)) = 1. Then, given a message m,
an integer on the range 0 < m <n, the message is encrypted by computing me (mod n) and the resulting cipher-text c is
decrypted by computing cd (mod n).

The standard definition of RSA cryptography is known as PKCS #1 [http://www.rsa.com/rsalabs/node.asp?id=2125]. It
provides a method for converting a text message to a number m suitable for encryption, and converting it back to the
original text message. It is also possible to use RSA to provide non-forgeable signatures; the basic idea is that the
sender encrypts a message hash with his decryption key, so the receiver can decrypt the message hash with the sender’s
public key, which works because only the sender knows his private decryption key.

Your task is to write an RSA key generator and procedures to encrypt and decrypt messages using the RSA algorithm.

Here is the RSA wiki [http://en.wikipedia.org/wiki/Rsa] to help you in understanding.
"""


def main():
    pass


if __name__ == "__main__":
    main()
