# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- New upcoming features currently in development.

### Fixed
- Pending bug fixes.

---

## [2.0.0] - 2026-10-28

### Added
- **Multi-Platform Universal Support**: Added native targets for Windows, Android, macOS, and iOS.
- **Interactive Web Portal**: Deployed responsive web hub on Firebase Hosting with 3D isometric platform cards.
- **On-Screen QR Hub**: Dual QR code switcher for instant mobile installation.
- **Automated CI/CD**: Cloud builds for macOS DMG and iOS IPA via GitHub Actions.
- **Automated Security**: Enabled CodeQL static analysis, Secret Scanning, and Dependabot version updates.

### Changed
- Migrated heavy binary distribution to GitHub Releases global CDN to eliminate hosting bandwidth bottlenecks.
- Hardened Content Security Policy (CSP) and HSTS preloading.

### Fixed
- Resolved non-exhaustive Swift switch statement in mascot model.
- Fixed Actions workflow permissions to enforce least-privilege token access (`contents: read`).

---

## [1.0.0] - 2026-10-15

### Added
- Initial standalone release for Windows.
- Basic hydration goal tracking and periodic desktop reminders.
