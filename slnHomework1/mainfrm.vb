Public Class mainfrm
    Public costDetails As New SortedList(Of String, Decimal)
    Public ticketDetails As New SortedList(Of String, Integer)

    Const morningPrice As Double = 10.99
    Const matineePrice As Double = 12.99
    Const eveningPrice As Double = 15.99
    Dim totalCost As Decimal 'Class/Module level var to store total cost.
    Dim numoftkts As Integer

    Private Sub btnBuy_Click(sender As Object, e As EventArgs) Handles btnBuy.Click
        Dim nameCust As String
        Dim showtime As Integer
        Dim validInput As Boolean
        Dim movieName As String

        validInput = ValidateName() AndAlso ValidateNumTickets()
        nameCust = txtName.Text
        showtime = cboDestination.SelectedIndex
        movieName = cboMovie.Text

        If validInput Then
            calculateShowCost(numoftkts, totalCost, showtime)
            lblOutputGreet.Text = nameCust & ", Thank you, Enjoy your " & cboDestination.SelectedItem & " Show!"
            lblOutputCost.Text = "The total cost is $" & totalCost
        End If

        UpdateTicketsList(movieName, totalCost)
        UpdateTicketNumbers(movieName, numoftkts)
    End Sub

    Private Sub calculateShowCost(ByVal numoftkts As Integer, ByRef DecTotalCost As Decimal, ByVal showtime As Integer)

        Select Case showtime
            Case 0
                DecTotalCost = morningPrice * numoftkts
            Case 1
                DecTotalCost = matineePrice * numoftkts
            Case 2
                DecTotalCost = eveningPrice * numoftkts
            Case Else
                MsgBox("Please choose showtime")
        End Select
    End Sub

    Private Sub clearBtn_Click(sender As Object, e As EventArgs) Handles clearBtn.Click
        txtName.Clear()
        txtNumOfTickets.Clear()
        lblOutputGreet.Text = ""
        lblOutputCost.Text = ""
        cboDestination.Text = "Select Show Time"
        cboMovie.Text = "Select Movie"
        mainPanel.Visible = False
    End Sub

    Private Sub exitBtn_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Application.Exit()
    End Sub
    Private Sub cboDestination_SelectedIndexChanged(sender As Object, e As EventArgs) Handles cboDestination.SelectedIndexChanged
        mainPanel.Visible = True
        cboMovie.Visible = True
    End Sub
    Private Function ValidateName() As Boolean
        Dim blnvalid As Boolean = False
        Dim nullvalid As Boolean = False
        Dim numericvalid As Boolean = False

        'Check if name is null
        If (txtName.Text = "") Then
            MsgBox("Name can't be null")
            txtName.Clear()
            txtName.Focus()
            nullvalid = False
        Else
            nullvalid = True
        End If

        'Check if name is numeric
        If IsNumeric(txtName.Text) Then
            MsgBox("Name can't be all numbers")
            txtName.Clear()
            txtName.Focus()
            numericvalid = False
        Else
            numericvalid = True
        End If

        If nullvalid And numericvalid = True Then
            blnvalid = True
        End If
        Return blnvalid
    End Function

    Private Function ValidateNumTickets() As Boolean
        'checks if only numbers are entered for number of people
        Dim blnValid As Boolean = False

        Try
            numoftkts = CInt(txtNumOfTickets.Text) 'Num of people is stored by VB in the text property
            If numoftkts > 0 Then
                blnValid = True
            Else
                MsgBox("Please enter number of tickets bigger than 0")
                blnValid = False
            End If

        Catch ex As InvalidCastException
            MsgBox("Invalid Cast Exception")

        Catch ex As FormatException
            MsgBox("Format Exception")

        Catch ex As OverflowException
            MsgBox("Overflow Exception")

        Catch ex As SystemException
            MsgBox("System Exception")

        End Try

        txtNumOfTickets.Focus()
        txtNumOfTickets.Clear()

        Return blnValid

    End Function

    Private Sub UpdateTicketsList(ByVal name As String, ByVal totalcost As Decimal)

        'procedure to update the sorted list 

        If costDetails.ContainsKey(name) Then
            costDetails(name) += totalcost
        Else
            costDetails.Add(name, totalcost)
        End If

    End Sub

    Private Sub UpdateTicketNumbers(ByVal name As String, ByVal numoftkts As Integer)

        If ticketDetails.ContainsKey(name) Then
            ticketDetails(name) += numoftkts
        Else
            ticketDetails.Add(name, numoftkts)
        End If

    End Sub

    Private Sub frmMain_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Dim movieArray = {"Leon", "God Father", "Squid Game", "Batman", "Spiderman"}

        For i = 0 To movieArray.Length - 1
            cboMovie.Items(i) = movieArray(i)
        Next
    End Sub

    Private Sub frmStats_Click(sender As Object, e As EventArgs) Handles frmStats.Click
        Dim statsfrm As New frmStatistics
        statsfrm.ShowDialog()
    End Sub

End Class

