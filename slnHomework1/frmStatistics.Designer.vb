<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmStatistics
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.btnReturn = New System.Windows.Forms.Button()
        Me.lstvTickets = New System.Windows.Forms.ListView()
        Me.lstvCost = New System.Windows.Forms.ListView()
        Me.lblTkts = New System.Windows.Forms.Label()
        Me.lblCost = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'btnReturn
        '
        Me.btnReturn.Location = New System.Drawing.Point(573, 609)
        Me.btnReturn.Name = "btnReturn"
        Me.btnReturn.Size = New System.Drawing.Size(201, 79)
        Me.btnReturn.TabIndex = 0
        Me.btnReturn.Text = "Return to Main"
        Me.btnReturn.UseVisualStyleBackColor = True
        '
        'lstvTickets
        '
        Me.lstvTickets.HideSelection = False
        Me.lstvTickets.Location = New System.Drawing.Point(429, 90)
        Me.lstvTickets.Name = "lstvTickets"
        Me.lstvTickets.Size = New System.Drawing.Size(464, 209)
        Me.lstvTickets.TabIndex = 1
        Me.lstvTickets.UseCompatibleStateImageBehavior = False
        '
        'lstvCost
        '
        Me.lstvCost.HideSelection = False
        Me.lstvCost.Location = New System.Drawing.Point(429, 367)
        Me.lstvCost.Name = "lstvCost"
        Me.lstvCost.Size = New System.Drawing.Size(464, 180)
        Me.lstvCost.TabIndex = 2
        Me.lstvCost.UseCompatibleStateImageBehavior = False
        '
        'lblTkts
        '
        Me.lblTkts.AutoSize = True
        Me.lblTkts.Location = New System.Drawing.Point(598, 47)
        Me.lblTkts.Name = "lblTkts"
        Me.lblTkts.Size = New System.Drawing.Size(143, 20)
        Me.lblTkts.TabIndex = 3
        Me.lblTkts.Text = "Movies and Tickets"
        '
        'lblCost
        '
        Me.lblCost.AutoSize = True
        Me.lblCost.Location = New System.Drawing.Point(584, 331)
        Me.lblCost.Name = "lblCost"
        Me.lblCost.Size = New System.Drawing.Size(157, 20)
        Me.lblCost.TabIndex = 4
        Me.lblCost.Text = "Movies and Revenue"
        '
        'frmStatistics
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(9.0!, 20.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1396, 814)
        Me.Controls.Add(Me.lblCost)
        Me.Controls.Add(Me.lblTkts)
        Me.Controls.Add(Me.lstvCost)
        Me.Controls.Add(Me.lstvTickets)
        Me.Controls.Add(Me.btnReturn)
        Me.Name = "frmStatistics"
        Me.Text = "Form2"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents btnReturn As Button
    Friend WithEvents lstvTickets As ListView
    Friend WithEvents lstvCost As ListView
    Friend WithEvents lblTkts As Label
    Friend WithEvents lblCost As Label
End Class
