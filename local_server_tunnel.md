# 本地服务器+内网穿透方案（临时分享）

## 一、方案说明

本地服务器+内网穿透是一种**临时分享**方案，适合：
- 需要快速分享给微信好友
- 不需要长期稳定访问
- 希望实时展示修改内容

## 二、准备工作

### 1. 确认Python已安装
```bash
python --version
```

### 2. 安装Node.js（用于localtunnel）
- 访问 [Node.js官网](https://nodejs.org/zh-cn/)
- 下载并安装LTS版本
- 验证安装：
  ```bash
  node --version
  npm --version
  ```

## 三、启动本地服务器

1. 进入项目目录
```bash
cd c:\Users\73200\Documents\trae_projects\PW
```

2. 启动HTTP服务器
```bash
# 使用Python启动服务器，端口8000
python -m http.server 8000
```

3. 验证本地访问
   - 打开浏览器，访问 `http://localhost:8000/ticket_agent_trainer.html`
   - 确认页面可以正常显示

## 四、使用localtunnel实现内网穿透

### 1. 安装localtunnel
```bash
npm install -g localtunnel
```

### 2. 启动内网穿透
```bash
# 将本地8000端口穿透到公网
lt --port 8000
```

### 3. 获取公网链接
- 命令执行后，会显示类似 `https://xxxx.loca.lt` 的公网链接
- 复制这个链接

## 五、微信分享

1. 将获取到的公网链接（如：`https://xxxx.loca.lt/ticket_agent_trainer.html`）分享给微信好友
2. 好友点击链接后即可在微信浏览器中查看和使用票务人设培训模拟器

## 六、注意事项

1. **临时性质**：localtunnel提供的链接在服务器关闭后会失效
2. **访问速度**：取决于你的网络环境
3. **安全性**：不建议用于敏感数据传输
4. **稳定性**：长时间运行可能会断开连接，需要重新启动

## 七、替代方案

### 方案1：使用ngrok

1. 访问 [ngrok官网](https://ngrok.com/)
2. 注册账号并下载ngrok
3. 解压后运行：
   ```bash
   ngrok http 8000
   ```
4. 获取公网链接并分享

### 方案2：使用花生壳

1. 访问 [花生壳官网](https://hsk.oray.com/)
2. 下载并安装花生壳客户端
3. 注册账号并登录
4. 创建免费域名并映射到本地8000端口
5. 使用分配的域名分享

## 八、关闭服务

1. 按 `Ctrl+C` 关闭localtunnel
2. 按 `Ctrl+C` 关闭本地HTTP服务器
