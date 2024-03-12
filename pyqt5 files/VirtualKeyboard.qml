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
        color: "transparent"
        opacity: 0.8

        Rectangle {
            width: parent.width
            height: 1
            color: "#e0e0e0"
            anchors.bottom: parent.bottom
        }

        Rectangle {
            width: parent.width
            height: 1
            color: "#e0e0e0"
            anchors.bottom: inputPanel.top
        }

        GridView {
            id: gridView
            width: parent.width
            height: parent.height - 2
            model: inputPanel.inputContext.inputItemModel
            delegate: Item {
                width: gridView.cellWidth
                height: gridView.cellHeight
                Rectangle {
                    width: parent.width
                    height: 1
                    color: "#e0e0e0"
                    anchors.bottom: parent.bottom
                }
                Rectangle {
                    width: parent.width
                    height: 1
                    color: "#e0e0e0"
                    anchors.bottom: inputPanel.top
                }
                Rectangle {
                    width: parent.width
                    height: 1
                    color: "#e0e0e0"
                    anchors.bottom: parent.bottom
                }
                Rectangle {
                    width: parent.width
                    height: 1
                    color: "#e0e0e0"
                    anchors.bottom: inputPanel.top
                }
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