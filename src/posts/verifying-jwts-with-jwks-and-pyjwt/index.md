---
title: Verifying JWTs with JWKs and PyJWT
description: How to verify a JWT signed with RS256 using a JWK and PyJWT.
date: 2019-03-17T16:38:35-04:00
lastmod: 2019-03-17T16:38:35-04:00
---

A JSON Web Key (JWK) is a JSON object representing a public key. You can use one to verify a JWT issued by an OIDC provider signing its tokens with RS256. A JWK Set (JWKS) is a JSON object containing an array of public keys in use by an OIDC provider. See the JWK spec, [RFC 7517](https://tools.ietf.org/html/rfc7517), for official definitions.

You can use [PyJWT](https://github.com/jpadilla/pyjwt) to verify an asymmetrically-signed JWT with a JWK. Sadly, you wouldn't know it by reading PyJWT's docs. The library's JWK support is undocumented. However, if you're using PyJWT and need to verify a JWT signed with RS256, chances are good you'll need to use a JWK to do so.

OIDC providers list a `jwks_uri` in the [discovery document](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata) found at `/.well-known/openid-configuration`. A GET request to the `jwks_uri` (e.g., `/.well-known/jwks.json`) returns the provider's JWKS. It might look something like:

```json
{
  "keys": [
    {
      "alg": "RS256",
      "kty": "RSA",
      "use": "sig",
      "x5c": [
        "x509-certificate-chain"
      ],
      "n": "modulus",
      "e": "exponent",
      "kid": "key-id",
      "x5t": "x509-certificate-thumbprint"
    }
  ]
}
```

This JWKS contains one JWK, but you should always assume that a JWKS will contain multiple keys. This can happen when, for example, a provider is rotating signing keys. To use a JWKS to verify a JWT, you need to parse the keys it contains. PyJWT can help you do this. Make a dictionary mapping each key's ID (`kid`) to its parsed representation:

```python
import json
import jwt

public_keys = {}
for jwk in jwks['keys']:
    kid = jwk['kid']
    public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
```

The `kid` property also appears in JWT headers. Use it to look up the public key corresponding to the private key with which your token was signed.

```python
kid = jwt.get_unverified_header(token)['kid']
key = public_keys[kid]
```

Finally, use that key to verify and decode your token:

```python
payload = jwt.decode(token, key=key, algorithms=['RS256'])
```

To avoid [algorithm confusion attacks](https://snikt.net/blog/2019/05/16/jwt-signature-vs-mac-attacks/), always specify the algorithm you expect to use for verification. Never fall back to the algorithm declared in the token!
