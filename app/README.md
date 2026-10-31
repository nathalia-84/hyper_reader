# Hyper Reader app

Flutter app (Android, portrait only). Flutter is pinned with fvm (see `.fvmrc`).

## Commands

Run from this directory:

```sh
fvm flutter pub get                 # also generates localizations (lib/l10n)
fvm dart run build_runner build     # regenerate drift code after schema changes
fvm flutter analyze
fvm flutter test
fvm flutter run                     # on a connected Android device
```

## Notes

- UI strings live in `lib/l10n/app_en.arb` (English only in the MVP).
- The Literata font is bundled under `assets/fonts/literata` (SIL Open Font License, see `OFL.txt`).
