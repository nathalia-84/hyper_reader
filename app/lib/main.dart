import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:hyper_reader/app.dart';
import 'package:hyper_reader/data/app_database.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]);

  final database = AppDatabase.onDevice();
  // Open the database now so a broken file fails at startup, not mid-read.
  await database.customSelect('SELECT 1').get();

  runApp(
    ProviderScope(
      overrides: [appDatabaseProvider.overrideWithValue(database)],
      child: const HyperReaderApp(),
    ),
  );
}
