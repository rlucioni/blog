---
title: "Verifying JWTs with JWKS and PyJWT"
date: 2019-03-17T16:38:35-04:00
lastmod: 2019-03-17T16:38:35-04:00
description: How to verify a JWT signed with RS256 using a JWKS and PyJWT.
draft: true
---

You wouldn't know it by reading the docs, but you can verify JWTs signed with RS256 using a JWKS and [PyJWT](https://github.com/jpadilla/pyjwt).

PyJWT's JWK support is undocumented. Important if trying to verify JWTs signed with RS256.

definitions directly from the spec, [RFC 7517](https://tools.ietf.org/html/rfc7517)

JSON Web Key (JWK): A JSON object that represents a cryptographic key.  The members of the object represent properties of the key, including its value.

JWK Set: A JSON object that represents a set of JWKs.  The JSON object MUST have a "keys" member, which is an array of JWKs.

A JWKS is an array of public keys used to verify a JWT issued by an authorization server. OIDC providers include a JWKS endpoint in the [OIDC discovery document](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig) commonly found at `/.well-known/openid-configuration`.

Auth0 exposes a JWKS endpoint for each tenant, which is found at https://your-tenant.auth0.com/.well-known/jwks.json. This endpoint will contain the JWK used to sign all Auth0 issued JWTs for this tenant. Here is an example of the JWKS used by a demo tenant.

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
