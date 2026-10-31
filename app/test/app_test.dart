import 'package:drift/drift.dart' show QueryRow;
import 'package:drift/native.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:hyper_reader/app.dart';
import 'package:hyper_reader/data/app_database.dart';

void main() {
  late AppDatabase database;

  setUp(() {
    database = AppDatabase(NativeDatabase.memory());
  });

  tearDown(() async {
    await database.close();
  });

  Future<void> pumpApp(WidgetTester tester) async {
    await tester.pumpWidget(
      ProviderScope(
        overrides: [appDatabaseProvider.overrideWithValue(database)],
        child: const HyperReaderApp(),
      ),
    );
    await tester.pumpAndSettle();
  }

  testWidgets('opens on an empty Library', (tester) async {
    await pumpApp(tester);

    expect(find.text('Library'), findsOneWidget);
    expect(find.text('No books yet'), findsOneWidget);
  });

  testWidgets('ignores the system font scale', (tester) async {
    tester.platformDispatcher.textScaleFactorTestValue = 2.0;
    addTearDown(tester.platformDispatcher.clearTextScaleFactorTestValue);

    await pumpApp(tester);

    final context = tester.element(find.text('No books yet'));
    expect(MediaQuery.textScalerOf(context), TextScaler.noScaling);
  });

  testWidgets('uses the fixed dark reading theme', (tester) async {
    await pumpApp(tester);

    final context = tester.element(find.text('No books yet'));
    final theme = Theme.of(context);
    expect(theme.brightness, Brightness.dark);
    expect(theme.scaffoldBackgroundColor, const Color(0xFF121212));
    expect(theme.textTheme.bodyLarge?.color, const Color(0xFFE0E0E0));
    expect(theme.textTheme.bodyLarge?.fontFamily, 'Literata');
  });

  test('the database opens', () async {
    expect(await database.customSelect('SELECT 1 AS one').getSingle(),
        isA<QueryRow>());
  });
}
