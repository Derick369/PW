# GitHub Pages部署指南（微信分享最佳方案）

## 一、准备工作

### 1. 创建GitHub账户
- 访问 [GitHub官网](https://github.com)
- 点击右上角「Sign up」创建账户
- 完成邮箱验证和账户设置

### 2. 安装Git（已安装可跳过）
- 访问 [Git官网](https://git-scm.com/downloads)
- 下载并安装适合Windows的Git版本
- 安装时保持默认选项即可

## 二、创建GitHub仓库

1. 登录GitHub后，点击右上角「+」号，选择「New repository」
2. 仓库名称：建议使用 `ticket-agent-trainer` 或其他有意义的名称
3. 仓库描述：可选，如「票务人设培训模拟器」
4. 选择「Public」（公开仓库）
5. 勾选「Initialize this repository with a README」
6. 点击「Create repository」

## 三、配置本地Git

### 1. 设置Git用户信息
```bash
# 替换为你的GitHub用户名和邮箱
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

### 2. 克隆仓库到本地
```bash
# 替换为你创建的仓库地址
git clone https://github.com/你的用户名/你的仓库名.git
```

## 四、上传项目文件

1. 进入克隆的仓库目录
```bash
cd 你的仓库名
```

2. 复制所有项目文件到仓库目录
   - 将 `ticket_agent_trainer.html`、`ticket_simulator.css` 等文件复制到仓库目录
   - 保持文件结构不变

3. 提交并推送文件
```bash
# 查看文件状态
git status

# 添加所有文件
git add .

# 提交文件
git commit -m "Initial commit of ticket agent trainer"

# 推送到GitHub
git push origin main
```

## 五、启用GitHub Pages

1. 回到GitHub仓库页面
2. 点击「Settings」选项卡
3. 在左侧菜单中选择「Pages」
4. 在「Source」部分：
   - 选择分支：`main`
   - 选择目录：`/(root)`
5. 点击「Save」
6. 等待几秒钟，页面会刷新并显示部署后的URL

## 六、微信分享

1. 复制GitHub Pages提供的URL（格式：`https://你的用户名.github.io/你的仓库名/ticket_agent_trainer.html`）
2. 在微信中直接分享这个链接给好友或朋友圈
3. 好友点击链接后即可在微信浏览器中查看和使用票务人设培训模拟器

## 七、后续更新

如果需要更新内容：

1. 修改本地文件
2. 提交并推送更新
```bash
git add .
git commit -m "Update content"
git push origin main
```
3. GitHub Pages会自动重新部署，几分钟后更新生效

## 八、注意事项

1. GitHub Pages是完全免费的静态网站托管服务
2. 每个GitHub账户可以创建多个GitHub Pages站点
3. 支持自定义域名（可选）
4. 微信可能会拦截部分非HTTPS链接，但GitHub Pages默认使用HTTPS，所以可以正常访问
