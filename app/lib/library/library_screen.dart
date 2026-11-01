import 'package:flutter/material.dart';
import 'package:hyper_reader/l10n/app_localizations.dart';

class LibraryScreen extends StatelessWidget {
  const LibraryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(l10n.libraryTitle)),
      body: Center(child: Text(l10n.libraryEmpty)),
    );
  }
}
