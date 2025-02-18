# Changelog

## v0.4.0

### [0.4.0](https://github.com/openfga/python-sdk/compare/v0.3.4...v0.4.0) (2024-01-11)

- feat: support for [conditions](https://openfga.dev/blog/conditional-tuples-announcement)
- chore!: use latest API interfaces for type info
- chore: add [example project](./example)
- chore: dependency updates

BREAKING CHANGES:
Note: This release comes with substantial breaking changes, especially to the interfaces due to the protobuf changes in the last release.

While the http interfaces did not break (you can still use `v0.3.3` SDK with a `v1.3.8+` server),
the grpc interface did and this caused a few changes in the interfaces of the SDK.

If you are using `OpenFgaClient`, the changes required should be smaller, if you are using `OpenFgaApi` a bit more changes will be needed.

You will have to modify some parts of your code, but we hope this will be to the better as a lot of the parameters are now correctly marked as required,
and so the Pointer-to-String conversion is no longer needed.

Some of the changes to expect:
- The following request interfaces changed:
    - `CheckRequest`: the `TupleKey` field is now of interface `CheckRequestTupleKey`, you can also now pass in `Context`
    - `ExpandRequest`: the `TupleKey` field is now of interface `ExpandRequestTupleKey`
    - `ReadRequest`: the `TupleKey` field is now of interface `ReadRequestTupleKey`
    - `WriteRequest`: now takes `WriteRequestWrites` and `WriteRequestDeletes`, the latter of which accepts `TupleKeyWithoutCondition`
    - And more
- The following interfaces had fields that were optional are are now required:
    - `CreateStoreResponse`
    - `GetStoreResponse`
    - `ListStoresResponse`
    - `ListObjectsResponse`
    - `ReadChangesResponse`
    - `ReadResponse`
    - `AuthorizationModel`
    - And more

Take a look at the changes in models in https://github.com/openfga/python-sdk/commit/9ed1f70d64db71451de2eb26e330bbd511625c5c and https://github.com/openfga/python-sdk/pull/59/files for more.

## v0.3.4

### [0.3.4](https://github.com/openfga/python-sdk/compare/v0.3.3...v0.3.4) (2024-01-09)

Note: `v0.3.4` has been re-released as `v0.4.0` due to breaking changes

## v0.3.3

### [0.3.3](https://github.com/openfga/python-sdk/compare/v0.3.2...v0.3.3) (2024-01-02)
- fix: correct type hints for list_relations
- fix: handle empty TupleKey in read
- chore: add example project

## v0.3.2

### [0.3.2](https://github.com/openfga/python-sdk/compare/v0.3.1...v0.3.2) (2023-12-15)
- feat: allow passing ssl certs to client configuration
- feat: setup openfga_sdk.help for bug info

## v0.3.1

### [0.3.1](https://github.com/openfga/python-sdk/compare/v0.3.0...v0.3.1) (2023-12-01)
- chore(deps): reduce min urllib3 to 1.25.11, add dependabot & bump deps

## v0.3.0

### [0.3.0](https://github.com/openfga/python-sdk/compare/v0.2.1...v0.3.0) (2023-11-02)
- feat(client): introduce synchronous OpenFgaClient (https://github.com/openfga/python-sdk/commit/c92b436543e263f2c1af6af15f1c4fda1c9dad21)
- refactor(config): extract oauth2 from credentials, removing logic from credentials configuration (https://github.com/openfga/python-sdk/commit/f91d14b25f86dd3f2e4d48229bb53cc7d9b20f1b)
- feat(client): performance improvements to batch_check (https://github.com/openfga/python-sdk/commit/d8f2d429d2c279c0e56d5ef2a6172df8bfadd82b)

## v0.2.1

### [0.2.1](https://github.com/openfga/python-sdk/compare/v0.2.0...v0.2.1) (2023-09-05)
- fix(client): fix a crash when calling check with contextual tuples (https://github.com/openfga/python-sdk/commit/dded83f9a75dc1f01c1cfbd8385a25654129f78f)
- chore(docs): update README and fix a few typos (https://github.com/openfga/python-sdk/pull/21, https://github.com/openfga/python-sdk/pull/31, https://github.com/openfga/python-sdk/pull/32, https://github.com/openfga/python-sdk/pull/33, https://github.com/openfga/python-sdk/pull/34, https://github.com/openfga/python-sdk/pull/37)

## v0.2.0

### [0.2.0](https://github.com/openfga/python-sdk/compare/v0.1.1...v0.2.0) (2023-05-25)

Changes:
- [BREAKING] feat!: `schema_version` is now required when calling `write_authorization_model`
- [BREAKING] chore!: drop support for python < 3.10
- feat(client): add OpenFgaClient wrapper see [docs](https://github.com/openfga/python-sdk/tree/main#readme), see the `v0.1.1` docs for [the OpenFgaApi docs](https://github.com/openfga/python-sdk/tree/v0.1.1#readme)
- feat(client): implement `batch_check` to check multiple tuples in parallel
- feat(client): implement `list_relations` to check in one call whether a user has multiple relations to an objects
- feat(client): add support for a non-transactional `write`
- feat(validation): ensure storeId and authorizationModelId are in valid ulid format
- chore(config): bump default max retries to `15`
- chore(deps): upgrade dependencies

## v0.1.1

### [0.1.1](https://github.com/openfga/python-sdk/compare/v0.1.0...v0.1.1) (2023-01-17)

- chore(deps): upgrade dependencies

## v0.1.0

### [0.1.0](https://github.com/openfga/python-sdk/compare/v0.0.1...v0.1.0) (2022-12-14)

Updated to include support for [OpenFGA 0.3.0](https://github.com/openfga/openfga/releases/tag/v0.3.0)

Changes:
- [BREAKING] feat(list-objects)!: response has been changed to include the object type
    e.g. response that was `{"object_ids":["roadmap"]}`, will now be `{"objects":["document:roadmap"]}`

Fixes:
- fix(models): update interfaces that had incorrectly optional fields to make them required


## v0.0.1

### [0.0.1](https://github.com/openfga/python-sdk/releases/tag/v0.0.1) (2022-08-31)

Initial OpenFGA Python SDK release
- Support for [OpenFGA](https://github.com/openfga/openfga) API
  - CRUD stores
  - Create, read & list authorization models
  - Writing and Reading Tuples
  - Checking authorization
  - Using Expand to understand why access was granted
