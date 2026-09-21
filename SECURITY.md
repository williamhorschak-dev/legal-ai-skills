# Security reporting and maintenance

Use GitHub's private vulnerability-reporting form under the repository's Security
tab for a reproducible software vulnerability. If private reporting is unavailable,
do not post credentials, case documents, or exploit details exposing private data
in a public issue. Report only the need for a private reporting channel.

Use synthetic examples and the smallest relevant reproduction. Include the skill
version, operating system, Python/host version, expected result, and observed
behavior. A prompt-injection report should identify the supplied source text and
the unauthorized behavior without including real confidential material.

General legal-reference corrections belong in ordinary issues with an official
public source. The project does not accept individual legal matters for review.
Security reporting does not create legal representation or a confidential intake
channel for a matter.

Direct Python requirements and GitHub Actions are pinned. Review transitive
dependency changes and relevant advisories before updating, then run the matrix
and affected regressions. A static scan, checksum, or pinned version is not a
guarantee that software has no vulnerability. Supported fixes target the latest
published release; preserve prior evidence when investigating a defect.
