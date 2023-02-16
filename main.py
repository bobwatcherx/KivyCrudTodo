from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import MDList,OneLineAvatarIconListItem,IconLeftWidget,IconRightWidget
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar

import uuid
class MyApp(MDApp):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.alldata = []
		self.mydialog = None


	def build(self):
		self.screen = Builder.load_file("load.kv")
		return self.screen

	# CREATE FUNCTION FOR ADD TODO TO LIST
	def addnewtodo(self,value):
		print("YOu input is = ",value)
		if value :
			# CREATE UUID FOR EDIT AND DELETE
			item_id = str(uuid.uuid4())
			self.alldata.append(
				{"value":value,"id":item_id}
				)

			# AND GET ID OF KV FILE MDLIST
			todo_list = self.screen.ids.todo_list
			# ADD TO WIDGET IN todo_list SELECTOR
			todo_list.add_widget(
				OneLineAvatarIconListItem(
					IconLeftWidget(
						icon="pencil",
						on_release=lambda x:self.editbtn(item_id,value)
						),
					IconRightWidget(
						icon="delete",
						on_release=lambda x:self.deletebtn(item_id)
						),
					id=item_id,
					text=value
					)

				)

		# AND CLEAR INPUT TEXT AFTER CLICK ADD BUTTON
		self.screen.ids.inputtodo.text = ""



	def editbtn(self,dataid,value):
		print("You Id FOr edit is ",dataid)
		self.editcontent = MDTextField(hint_text="update name",mode="fill")
		self.mylayout = MDBoxLayout(
			orientation="vertical",
			size_hint_y=0.8,
			height=300
			)
		# ADD EDITCONTENT TO LAYOUT BOXLAYOUT
		self.mylayout.add_widget(Label(text="edit data"))
		if not self.mydialog:
			self.dialog = MDDialog(
				title="edit data",
				type="custom",
				size_hint=(0.8,None),
				height=300,
				content_cls=self.mylayout,
				buttons=[
					MDFlatButton(
						text="save",
						text_color="red",
						on_release=lambda x:self.savenow(dataid,self.editcontent.text)

						)

				]

				)
		self.dialog.content_cls.add_widget(self.editcontent)
		self.dialog.open()

	def savenow(self,data,newvalue):
		# AND IF SUCCESS EDIT THEN SHOW SNACKBAR
		self.notif = Snackbar(
			text="success edit",
			font_size=30,
			bg_color=(0,0,1,1)

			)

		# AND CLOSE YOU DIALOG EDIT
		self.dialog.dismiss()

		# AND NOW EDIT self.alldata edit IN textfiled edit
		for x in self.alldata:
			if x['id'] == data:
				# data is ID FROM YOU LIST 
				x['value'] = newvalue

				# AND GET ID FROM TODO LIST FROM KV FILE
				todo_list = self.screen.ids.todo_list
				for child in todo_list.children:
					if child.id == data:
						child.text = newvalue

						# AND SHOW SNACKBAR
						self.notif.open()





	def deletebtn(self,data):
		# LOOP self.alldata  AND CHEK IF id == data id and removeit
		for x in self.alldata:
			if x['id'] == data:
				self.alldata.remove(x)
				print(self.alldata)

				# AND LIST ITEM IN KV FILE THE REMOVE UPDATE DATA
				todo_list = self.screen.ids.todo_list
				for child in todo_list.children:
					if child.id == data:
						todo_list.remove_widget(child)
					# DATA IS UNIQ ID FROM UUID4







if __name__ == "__main__":
	MyApp().run()
