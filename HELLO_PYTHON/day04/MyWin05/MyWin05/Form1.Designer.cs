namespace MyWin05
{
    partial class Form1
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblMine = new System.Windows.Forms.Label();
            this.lblCom = new System.Windows.Forms.Label();
            this.lblResult = new System.Windows.Forms.Label();
            this.tb1 = new System.Windows.Forms.TextBox();
            this.tb2 = new System.Windows.Forms.TextBox();
            this.tbResult = new System.Windows.Forms.TextBox();
            this.btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblMine
            // 
            this.lblMine.AutoSize = true;
            this.lblMine.Location = new System.Drawing.Point(68, 91);
            this.lblMine.Name = "lblMine";
            this.lblMine.Size = new System.Drawing.Size(25, 12);
            this.lblMine.TabIndex = 0;
            this.lblMine.Text = "나 :";
            this.lblMine.Click += new System.EventHandler(this.label1_Click);
            // 
            // lblCom
            // 
            this.lblCom.AutoSize = true;
            this.lblCom.Location = new System.Drawing.Point(68, 152);
            this.lblCom.Name = "lblCom";
            this.lblCom.Size = new System.Drawing.Size(25, 12);
            this.lblCom.TabIndex = 0;
            this.lblCom.Text = "컴 :";
            this.lblCom.Click += new System.EventHandler(this.label1_Click);
            // 
            // lblResult
            // 
            this.lblResult.AutoSize = true;
            this.lblResult.Location = new System.Drawing.Point(68, 237);
            this.lblResult.Name = "lblResult";
            this.lblResult.Size = new System.Drawing.Size(29, 12);
            this.lblResult.TabIndex = 1;
            this.lblResult.Text = "결과";
            // 
            // tb1
            // 
            this.tb1.Location = new System.Drawing.Point(127, 88);
            this.tb1.Name = "tb1";
            this.tb1.Size = new System.Drawing.Size(183, 21);
            this.tb1.TabIndex = 2;
            // 
            // tb2
            // 
            this.tb2.Location = new System.Drawing.Point(127, 149);
            this.tb2.Name = "tb2";
            this.tb2.Size = new System.Drawing.Size(183, 21);
            this.tb2.TabIndex = 3;
            // 
            // tbResult
            // 
            this.tbResult.Location = new System.Drawing.Point(127, 237);
            this.tbResult.Name = "tbResult";
            this.tbResult.Size = new System.Drawing.Size(183, 21);
            this.tbResult.TabIndex = 4;
            // 
            // btn
            // 
            this.btn.Location = new System.Drawing.Point(70, 306);
            this.btn.Name = "btn";
            this.btn.Size = new System.Drawing.Size(240, 41);
            this.btn.TabIndex = 5;
            this.btn.Text = "게임하기";
            this.btn.UseVisualStyleBackColor = true;
            this.btn.Click += new System.EventHandler(this.btn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(402, 455);
            this.Controls.Add(this.btn);
            this.Controls.Add(this.tbResult);
            this.Controls.Add(this.tb2);
            this.Controls.Add(this.tb1);
            this.Controls.Add(this.lblResult);
            this.Controls.Add(this.lblCom);
            this.Controls.Add(this.lblMine);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblMine;
        private System.Windows.Forms.Label lblCom;
        private System.Windows.Forms.Label lblResult;
        private System.Windows.Forms.TextBox tb1;
        private System.Windows.Forms.TextBox tb2;
        private System.Windows.Forms.TextBox tbResult;
        private System.Windows.Forms.Button btn;
    }
}

