Public Class frmStatistics
    Private Sub frmStatistics_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        lstvCost.View = View.Details
        lstvCost.GridLines = True
        lstvCost.FullRowSelect = True

        lstvCost.Columns.Add("Name", 100)
        lstvCost.Columns.Add("Total Spent", 100)


        lstvTickets.View = View.Details
        lstvTickets.GridLines = True
        lstvTickets.FullRowSelect = True

        lstvTickets.Columns.Add("Name", 100)
        lstvTickets.Columns.Add("Num of people", 100)


        Dim arr(1) As String 'length of the array = no of columns in the listview object 

        Dim itm As ListViewItem


        lstvCost.Items.Clear()
        Dim templist As New SortedList(Of String, Decimal)
        For Each m As KeyValuePair(Of String, Decimal) In mainfrm.costDetails
            'MsgBox("List contains" & frmMain.costDetails)
            arr(0) = m.Key
            arr(1) = m.Value.ToString
            itm = New ListViewItem(arr)
            lstvCost.Items.Add(itm)

        Next

        lstvTickets.Items.Clear()
        For Each m As KeyValuePair(Of String, Integer) In mainfrm.ticketDetails

            arr(0) = m.Key
            arr(1) = m.Value.ToString
            itm = New ListViewItem(arr)
            lstvTickets.Items.Add(itm)

        Next
    End Sub

    Private Sub btnReturn_Click(sender As Object, e As EventArgs) Handles btnReturn.Click

        Dim mainfrm As New mainfrm

        Hide()
        mainfrm.ShowDialog()
    End Sub

End Class