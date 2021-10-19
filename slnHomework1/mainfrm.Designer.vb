<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class mainfrm
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
        Me.PictureBox1 = New System.Windows.Forms.PictureBox()
        Me.txtName = New System.Windows.Forms.TextBox()
        Me.txtNumOfTickets = New System.Windows.Forms.TextBox()
        Me.nameLabel = New System.Windows.Forms.Label()
        Me.ticketLabel = New System.Windows.Forms.Label()
        Me.lblOutputGreet = New System.Windows.Forms.Label()
        Me.btnBuy = New System.Windows.Forms.Button()
        Me.clearBtn = New System.Windows.Forms.Button()
        Me.btnExit = New System.Windows.Forms.Button()
        Me.PictureBox2 = New System.Windows.Forms.PictureBox()
        Me.banner2 = New System.Windows.Forms.Label()
        Me.banner = New System.Windows.Forms.Label()
        Me.cboDestination = New System.Windows.Forms.ComboBox()
        Me.mainPanel = New System.Windows.Forms.Panel()
        Me.lblOutputCost = New System.Windows.Forms.Label()
        Me.cboMovie = New System.Windows.Forms.ComboBox()
        Me.frmStats = New System.Windows.Forms.Button()
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.PictureBox2, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.mainPanel.SuspendLayout()
        Me.SuspendLayout()
        '
        'PictureBox1
        '
        Me.PictureBox1.Image = Global.slnHomework1.My.Resources.Resources.theater
        Me.PictureBox1.Location = New System.Drawing.Point(-1, -3)
        Me.PictureBox1.Name = "PictureBox1"
        Me.PictureBox1.Size = New System.Drawing.Size(230, 646)
        Me.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        Me.PictureBox1.TabIndex = 0
        Me.PictureBox1.TabStop = False
        '
        'txtName
        '
        Me.txtName.Location = New System.Drawing.Point(174, 9)
        Me.txtName.Name = "txtName"
        Me.txtName.Size = New System.Drawing.Size(95, 26)
        Me.txtName.TabIndex = 3
        '
        'txtNumOfTickets
        '
        Me.txtNumOfTickets.Location = New System.Drawing.Point(174, 55)
        Me.txtNumOfTickets.Name = "txtNumOfTickets"
        Me.txtNumOfTickets.Size = New System.Drawing.Size(57, 26)
        Me.txtNumOfTickets.TabIndex = 4
        '
        'nameLabel
        '
        Me.nameLabel.AutoSize = True
        Me.nameLabel.Location = New System.Drawing.Point(99, 15)
        Me.nameLabel.Name = "nameLabel"
        Me.nameLabel.Size = New System.Drawing.Size(55, 20)
        Me.nameLabel.TabIndex = 5
        Me.nameLabel.Text = "Name:"
        '
        'ticketLabel
        '
        Me.ticketLabel.AutoSize = True
        Me.ticketLabel.Location = New System.Drawing.Point(13, 61)
        Me.ticketLabel.Name = "ticketLabel"
        Me.ticketLabel.Size = New System.Drawing.Size(141, 20)
        Me.ticketLabel.TabIndex = 6
        Me.ticketLabel.Text = "Number of Tickets:"
        '
        'lblOutputGreet
        '
        Me.lblOutputGreet.AutoSize = True
        Me.lblOutputGreet.Location = New System.Drawing.Point(29, 109)
        Me.lblOutputGreet.Name = "lblOutputGreet"
        Me.lblOutputGreet.Size = New System.Drawing.Size(0, 20)
        Me.lblOutputGreet.TabIndex = 7
        '
        'btnBuy
        '
        Me.btnBuy.Location = New System.Drawing.Point(500, 9)
        Me.btnBuy.Name = "btnBuy"
        Me.btnBuy.Size = New System.Drawing.Size(145, 74)
        Me.btnBuy.TabIndex = 8
        Me.btnBuy.Text = "Buy"
        Me.btnBuy.UseVisualStyleBackColor = True
        '
        'clearBtn
        '
        Me.clearBtn.Location = New System.Drawing.Point(500, 97)
        Me.clearBtn.Name = "clearBtn"
        Me.clearBtn.Size = New System.Drawing.Size(145, 70)
        Me.clearBtn.TabIndex = 9
        Me.clearBtn.Text = "Clear"
        Me.clearBtn.UseVisualStyleBackColor = True
        '
        'btnExit
        '
        Me.btnExit.Location = New System.Drawing.Point(953, 485)
        Me.btnExit.Name = "btnExit"
        Me.btnExit.Size = New System.Drawing.Size(103, 44)
        Me.btnExit.TabIndex = 10
        Me.btnExit.Text = "Exit"
        Me.btnExit.UseVisualStyleBackColor = True
        '
        'PictureBox2
        '
        Me.PictureBox2.BackColor = System.Drawing.Color.Gray
        Me.PictureBox2.Location = New System.Drawing.Point(235, -3)
        Me.PictureBox2.Name = "PictureBox2"
        Me.PictureBox2.Size = New System.Drawing.Size(912, 126)
        Me.PictureBox2.TabIndex = 13
        Me.PictureBox2.TabStop = False
        '
        'banner2
        '
        Me.banner2.AutoSize = True
        Me.banner2.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!)
        Me.banner2.Location = New System.Drawing.Point(500, 65)
        Me.banner2.Name = "banner2"
        Me.banner2.Size = New System.Drawing.Size(436, 25)
        Me.banner2.TabIndex = 15
        Me.banner2.Text = "10:30am $10.99, 3:30pm $12.99, 6:30pm $15.99"
        '
        'banner
        '
        Me.banner.AutoSize = True
        Me.banner.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!)
        Me.banner.Location = New System.Drawing.Point(581, 9)
        Me.banner.Name = "banner"
        Me.banner.Size = New System.Drawing.Size(284, 29)
        Me.banner.TabIndex = 14
        Me.banner.Text = "Welcome to ABC Movies!"
        '
        'cboDestination
        '
        Me.cboDestination.FormattingEnabled = True
        Me.cboDestination.Items.AddRange(New Object() {"10:30am Morning", "3:30pm Matinee", "6:30pm Evening"})
        Me.cboDestination.Location = New System.Drawing.Point(489, 150)
        Me.cboDestination.Name = "cboDestination"
        Me.cboDestination.Size = New System.Drawing.Size(176, 28)
        Me.cboDestination.TabIndex = 16
        Me.cboDestination.Text = "Select Show Time"
        '
        'mainPanel
        '
        Me.mainPanel.BackColor = System.Drawing.SystemColors.ActiveCaption
        Me.mainPanel.Controls.Add(Me.lblOutputCost)
        Me.mainPanel.Controls.Add(Me.txtNumOfTickets)
        Me.mainPanel.Controls.Add(Me.txtName)
        Me.mainPanel.Controls.Add(Me.nameLabel)
        Me.mainPanel.Controls.Add(Me.ticketLabel)
        Me.mainPanel.Controls.Add(Me.btnBuy)
        Me.mainPanel.Controls.Add(Me.lblOutputGreet)
        Me.mainPanel.Controls.Add(Me.clearBtn)
        Me.mainPanel.Location = New System.Drawing.Point(396, 212)
        Me.mainPanel.Name = "mainPanel"
        Me.mainPanel.Size = New System.Drawing.Size(660, 199)
        Me.mainPanel.TabIndex = 17
        Me.mainPanel.Visible = False
        '
        'lblOutputCost
        '
        Me.lblOutputCost.AutoSize = True
        Me.lblOutputCost.Location = New System.Drawing.Point(29, 163)
        Me.lblOutputCost.Name = "lblOutputCost"
        Me.lblOutputCost.Size = New System.Drawing.Size(0, 20)
        Me.lblOutputCost.TabIndex = 9
        '
        'cboMovie
        '
        Me.cboMovie.FormattingEnabled = True
        Me.cboMovie.Items.AddRange(New Object() {"Movie A", "Movie B", "Movie C", "Movie D", "Movie E"})
        Me.cboMovie.Location = New System.Drawing.Point(792, 150)
        Me.cboMovie.Name = "cboMovie"
        Me.cboMovie.Size = New System.Drawing.Size(175, 28)
        Me.cboMovie.TabIndex = 18
        Me.cboMovie.Text = "Select Movie"
        Me.cboMovie.Visible = False
        '
        'frmStats
        '
        Me.frmStats.Location = New System.Drawing.Point(396, 485)
        Me.frmStats.Name = "frmStats"
        Me.frmStats.Size = New System.Drawing.Size(154, 44)
        Me.frmStats.TabIndex = 19
        Me.frmStats.Text = "Show Statistics"
        Me.frmStats.UseVisualStyleBackColor = True
        '
        'mainfrm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(9.0!, 20.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1150, 642)
        Me.Controls.Add(Me.frmStats)
        Me.Controls.Add(Me.cboMovie)
        Me.Controls.Add(Me.mainPanel)
        Me.Controls.Add(Me.cboDestination)
        Me.Controls.Add(Me.banner2)
        Me.Controls.Add(Me.banner)
        Me.Controls.Add(Me.PictureBox2)
        Me.Controls.Add(Me.btnExit)
        Me.Controls.Add(Me.PictureBox1)
        Me.Name = "mainfrm"
        Me.Text = "Form1"
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.PictureBox2, System.ComponentModel.ISupportInitialize).EndInit()
        Me.mainPanel.ResumeLayout(False)
        Me.mainPanel.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents PictureBox1 As PictureBox
    Friend WithEvents txtName As TextBox
    Friend WithEvents txtNumOfTickets As TextBox
    Friend WithEvents nameLabel As Label
    Friend WithEvents ticketLabel As Label
    Friend WithEvents btnBuy As Button
    Friend WithEvents clearBtn As Button
    Friend WithEvents btnExit As Button
    Friend WithEvents lblOutputGreet As Label
    Friend WithEvents PictureBox2 As PictureBox
    Friend WithEvents banner2 As Label
    Friend WithEvents banner As Label
    Friend WithEvents cboDestination As ComboBox
    Friend WithEvents mainPanel As Panel
    Friend WithEvents lblOutputCost As Label
    Friend WithEvents cboMovie As ComboBox
    Friend WithEvents frmStats As Button
End Class
