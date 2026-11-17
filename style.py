def use_style(app):
    app.setStyleSheet("""
QWidget {
    background-color: #E4E8F2;
    font-family: 'Sakkal Majalla';
    }
            

QGroupBox {
    background-color: #DCE8DF;
    border: 1px solid 080200;
    border-radius: 10px;
    margin-top: 15px;
    padding: 10px;
    font-size: 22px;
    font-weight: bold;
    }
QPushButton#btn_menu {
    background-color: #DCE8DF;
    color: #374151;
    border-radius: 8px;
    padding: 5px 14px;
    font-family: 'Sakkal Majalla';
    font-size: 34px;
    font-weight: bold;
}

QPushButton#btn_menu:hover {
    background-color: #DCE8DF;
    border-color: #8E8EDB;
}


QPushButton#btn_menu:checked {
    background-color: #DCE8DF;
    color: red;
    font-weight: bold;
}
QWidget#transp_page {background-color: #DCE8DF;}
QPushButton#simple_btn{
    background-color: #6B4F3A; 
    color: black;
    border: none;
    border-radius: 8px;
    padding: 8px;
    font-family: 'Sakkal Majalla';
    font-size: 38px;
    font-weight: bold;
    }

QPushButton#simple_btn:hover {
    color: white;
    }
QPushButton#simple_btn:pressed {
        background-color: #16213E;
    }
QComboBox {
    background-color: white;
    color: #2C3E50;
    border: 1px solid #B8C2CC;
    border-radius: 8px;
    padding: 6px 10px;
    min-height: 28px;
    font-family: "Sakkal Majalla";
    font-size: 28px;
    }

QComboBox:hover {
    border: 1px solid #3498DB;
    }

QComboBox:focus {
    border: 1px solid #2980B9;
    }

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 30px;
    border-left: 1px solid #D5DDE5;
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
    }

QComboBox QAbstractItemView {
    background-color: white;
    color: #2C3E50;
    selection-background-color: #D6EAF8;
    selection-color: #154360;
    border: 1px solid #B8C2CC;
    outline: 0;
    }
QLabel {
    background-color: transparent;
    color: #333333;
    font-family: "Sakkal Majalla";
    font-size: 25px;
    font-weight: bold;
    padding: 2px;
    }
""")
    