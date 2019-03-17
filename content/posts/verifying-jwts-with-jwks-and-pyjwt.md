---
title: "Verifying JWTs with JWKS and PyJWT"
date: 2019-03-17T16:38:35-04:00
lastmod: 2019-03-17T16:38:35-04:00
description: How to verify a JWT signed with RS256 using a JWKS and PyJWT.
draft: true
---

You can verify a JWT signed with RS256 (asymmetric encryption) using a JWKS and [PyJWT](https://github.com/jpadilla/pyjwt). Sadly, you wouldn't know it by reading PyJWT's docs. The library's JWK support is undocumented. However, if you're using PyJWT and need to verify a JWT signed with RS256, chances are good you'll need to use a JWKS to do so.

In the context of OIDC and JWTs, a JSON Web Key (JWK) is a JSON object representing a public key. You can use it to verify a JWT signed with RS256. A JWK Set (JWKS) is a JSON object containing all public keys in use by an OIDC provider. Every JWKS includes an array of JWKs under `keys`. See the JWK spec, [RFC 7517](https://tools.ietf.org/html/rfc7517), for official definitions.

OIDC providers list a `jwks_uri` in the [discovery document](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig) found at `/.well-known/openid-configuration`. A GET request to the `jwks_uri` (e.g., `/.well-known/jwks.json`) returns the provider's JWKS. It might look something like:

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

This JWKS contains one JWK, but you should always assume that a JWKS will contain multiple keys. This can happen when, for example, a provider is rotating signing keys.

To use this JWKS to verify a JWT, you need to parse the keys it contains first. PyJWT can help you do this. Make a dictionary mapping each key's ID (`kid`) to its parsed representation:

```python
import json

import jwt


public_keys = {}
for jwk in jwks['keys']:
    public_keys[jwk['kid']] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
```

The `kid` property also appears in JWT headers. Use it to look up the public key corresponding to the private key used to sign your token.

```python
kid = jwt.get_unverified_header(token)['kid']
key = public_keys[kid]
```

Now you can use that key to verify and decode your token:

```python
 payload = jwt.decode(token, key=key)
```

All together, the process might look like this:

```python
import json

import jwt
import requests


OIDC_AUTHORITY = 'https://oidc.example.com'
OIDC_CLIENT_ID = 'example'


def verify_token(token):
    kid = jwt.get_unverified_header(token)['kid']
    public_keys = get_public_keys()
    key = public_keys[kid]

    return jwt.decode(token, key=key, audience=OIDC_CLIENT_ID)


def get_public_keys():
    oidc_conf = requests.get(OIDC_AUTHORITY + '/.well-known/openid-configuration').json()
    jwks = requests.get(oidc_conf['jwks_uri']).json()

    public_keys = {}
    for jwk in jwks['keys']:
        public_keys[jwk['kid']] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    return public_keys
```
