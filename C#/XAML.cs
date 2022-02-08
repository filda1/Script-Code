XAML.cs

  StackPanel  p = new StackPanel()

   p.children.Add(MiLabel)

  this.content = p

 *****************************************************

 OJO. EN XAML.cs los Objetos pueden ser con:

 OBJETOS con CONTENT :

  Button
  View
  Label
  ...

 OBJETOS CON CHILDREN (Los que Utliza children es porque puede repetor Objetos):

 STACK
 GRID
 ...