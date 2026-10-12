class Document:
    def show_details(self):
        print("This is a generic document.")
        
class PDF(Document):
    def show_details(self):
        print("This is a PDF document")
        
class Word(Document):
    def show_details(self):
        print("This is a Word document")
        
obj_doc = Document()
obj_pdf = PDF()
obj_word = Word()

for doc in (obj_doc, obj_pdf, obj_word):
    doc.show_details()
    
