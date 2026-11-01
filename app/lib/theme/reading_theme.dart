import 'package:flutter/material.dart';

/// Fixed, non-configurable look of the app: always dark, soft black
/// background, off-white text and the bundled Literata serif.
abstract final class ReadingColors {
  static const background = Color(0xFF121212);
  static const text = Color(0xFFE0E0E0);
}

const readingFontFamily = 'Literata';

ThemeData buildReadingTheme() {
  final base = ThemeData(
    brightness: Brightness.dark,
    fontFamily: readingFontFamily,
    colorScheme: const ColorScheme.dark(
      surface: ReadingColors.background,
      onSurface: ReadingColors.text,
    ),
    scaffoldBackgroundColor: ReadingColors.background,
  );
  return base.copyWith(
    textTheme: base.textTheme.apply(
      bodyColor: ReadingColors.text,
      displayColor: ReadingColors.text,
    ),
    appBarTheme: const AppBarTheme(
      backgroundColor: ReadingColors.background,
      foregroundColor: ReadingColors.text,
    ),
  );
}
