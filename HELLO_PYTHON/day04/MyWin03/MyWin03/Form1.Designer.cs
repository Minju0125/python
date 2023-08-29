namespace MyWin03
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
            this.lbl = new System.Windows.Forms.Label();
            this.tb = new System.Windows.Forms.TextBox();
            this.btn = new System.Windows.Forms.Button();
            this.tbResult = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // lbl
            // 
            this.lbl.AutoSize = true;
            this.lbl.Location = new System.Drawing.Point(68, 46);
            this.lbl.Name = "lbl";
            this.lbl.Size = new System.Drawing.Size(29, 12);
            this.lbl.TabIndex = 0;
            this.lbl.Text = "단수";
            this.lbl.Click += new System.EventHandler(this.label1_Click);
            // 
            // tb
            // 
            this.tb.Location = new System.Drawing.Point(149, 43);
            this.tb.Name = "tb";
            this.tb.Size = new System.Drawing.Size(121, 21);
            this.tb.TabIndex = 1;
            // 
            // btn
            // 
            this.btn.Location = new System.Drawing.Point(70, 80);
            this.btn.Name = "btn";
            this.btn.Size = new System.Drawing.Size(200, 22);
            this.btn.TabIndex = 2;
            this.btn.Text = "출력하기";
            this.btn.UseVisualStyleBackColor = true;
            this.btn.Click += new System.EventHandler(this.btn_Click);
            // 
            // tbResult
            // 
            this.tbResult.Location = new System.Drawing.Point(70, 126);
            this.tbResult.Multiline = true;
            this.tbResult.Name = "tbResult";
            this.tbResult.Size = new System.Drawing.Size(200, 260);
            this.tbResult.TabIndex = 3;
            this.tbResult.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(338, 445);
            this.Controls.Add(this.tbResult);
            this.Controls.Add(this.btn);
            this.Controls.Add(this.tb);
            this.Controls.Add(this.lbl);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lbl;
        private System.Windows.Forms.TextBox tb;
        private System.Windows.Forms.Button btn;
        private System.Windows.Forms.TextBox tbResult;
    }
}

