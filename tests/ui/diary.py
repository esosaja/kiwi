from kiwi.ui.test.player import Player

player = Player(['examples/framework/diary/diary.py'])
app = player.get_app()

player.wait_for_window("Diary")
app.Diary.add.clicked()
app.Diary.title.set_text("New title")
app.Diary.title.set_text("")
app.Diary.title.set_text("F")
app.Diary.title.set_text("Fo")
app.Diary.title.set_text("Foo")
app.Diary.title.set_text("Foob")
app.Diary.title.set_text("Fooba")
app.Diary.title.set_text("Foobar")
app.Diary.add.clicked()
app.Diary.title.set_text("")
app.Diary.title.set_text("New title")
app.Diary.ObjectList.select_paths(['1'])
app.Diary.title.set_text("")
app.Diary.title.set_text("T")
app.Diary.title.set_text("Te")
app.Diary.title.set_text("Tes")
app.Diary.title.set_text("Test")
app.Diary.title.set_text("Testi")
app.Diary.title.set_text("Testin")
app.Diary.title.set_text("Testing")
app.Diary.title.set_text("")
app.Diary.title.set_text("Foobar")
app.Diary.ObjectList.select_paths(['0'])
app.Diary.remove.clicked()
app.Diary.ObjectList.select_paths([])
app.Diary.title.set_text("")
app.Diary.title.set_text("Testing")
app.Diary.ObjectList.select_paths(['0'])
app.Diary.period.clicked()
app.Diary.evening.clicked()
app.Diary.remove.clicked()
app.Diary.ObjectList.select_paths([])
player.delete_window("Diary")

player.finish()