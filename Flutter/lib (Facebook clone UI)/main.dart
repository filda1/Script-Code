//import 'package:dartspace/pages/home_page.dart';
import 'package:dartspace/pages/welcome_page.dart';
import 'package:flutter/material.dart';
import 'package:flutter_statusbarcolor/flutter_statusbarcolor.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    //color azul mas pequeno x por defecto, el primer azul del toollbar
    FlutterStatusbarcolor.setStatusBarColor(Colors.white);
    return MaterialApp(
      //title: 'dartspace',
      debugShowCheckedModeBanner: false,
      home: WelcomePage(),
    );
  }
}
