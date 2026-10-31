import 'package:drift/drift.dart';
import 'package:drift_flutter/drift_flutter.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

part 'app_database.g.dart';

/// The app's single SQLite database. Features add their tables here.
@DriftDatabase(tables: [])
class AppDatabase extends _$AppDatabase {
  AppDatabase(super.executor);

  /// Opens the on-device database file.
  AppDatabase.onDevice() : super(driftDatabase(name: 'hyper_reader'));

  @override
  int get schemaVersion => 1;
}

/// The database is created in `main` and injected via an override, so tests
/// can supply an in-memory one.
final appDatabaseProvider = Provider<AppDatabase>(
  (ref) => throw UnimplementedError('appDatabaseProvider must be overridden'),
);
