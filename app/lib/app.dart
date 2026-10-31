import 'package:flutter/material.dart';
import 'package:hyper_reader/l10n/app_localizations.dart';
import 'package:hyper_reader/library/library_screen.dart';
import 'package:hyper_reader/theme/reading_theme.dart';

class HyperReaderApp extends StatelessWidget {
  const HyperReaderApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      onGenerateTitle: (context) => AppLocalizations.of(context).appTitle,
      localizationsDelegates: AppLocalizations.localizationsDelegates,
      supportedLocales: AppLocalizations.supportedLocales,
      theme: buildReadingTheme(),
      themeMode: ThemeMode.dark,
      // The page layout is designed for one fixed text size, so the system
      // font-scale setting is ignored everywhere.
      builder: (context, child) => MediaQuery.withNoTextScaling(child: child!),
      home: const LibraryScreen(),
    );
  }
}
