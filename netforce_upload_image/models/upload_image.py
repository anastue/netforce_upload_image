import os

from netforce.model import Model, fields, get_model
from netforce.database import get_active_db

class UploadImage(Model):
    _name = "upload.image"
    _transient = True
    _fields = {
        'model' : fields.Char("model"),
        'next': fields.Char("Next"),
        'title': fields.Char("Title"),
        'file' : fields.File("ZIP File", required=True),
    }

    def default_get(self, fields_names=None, context=None, **kw):
        model = context["model_name"]
        m = get_model(model)
        title = "Upload Image"
        if m._string:
            title += " " + m._string
        return {
            "model": model,
            "title": title,
            "next": context.get("next"),
        }

    def do_upload(self, ids, context={}):
        obj = self.browse(ids[0])
        dbname = get_active_db()
        file_import = obj.file
        if not file_import:
            raise Exception("Please Define File")
        fdir = os.path.join("static", "db", dbname, "files")
        file_path_import = os.path.join(fdir, file_import)
        return

UploadImage.register()
