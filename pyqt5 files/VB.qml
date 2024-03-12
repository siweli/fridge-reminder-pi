import QtQuick 2.15
import QtQuick.VirtualKeyboard 2.15

InputPanel {
    id: inputPanel
    z: 99
    width: parent.width
    height: parent.height * 0.3
    y: parent.height - height

    Rectangle {
        width: parent.width
        height: parent.height
        
        opacity: 0.8

        GridView {
            id: gridView
            width: parent.width
            height: parent.height - 2
            model: inputPanel.inputItemModel
            delegate: Rectangle {
                width: gridView.cellWidth
                height: gridView.cellHeight
                color: "#FFFFFF"
                border.color: "#CCCCCC"
                Text {
                    text: model.display
                    anchors.centerIn: parent
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: inputPanel.inputContext.sendKey(model)
                }
            }
        }
    }
}
