# ATRIbot
一个主打osu查查查的bot

# 开发

## 基础建设

所有功能处理逻辑先对接`Core.py`

### 急急急

- [ ] MongoDB读写数据(需要制定规范标准)
- [ ] osuapiv2
- [ ] rosu查询谱面pp
  
### 不是很急的
- [ ] draw绘图
- [ ] FASTAPI包装
- [ ] Onebotv11对接

## MongoDB储存的数据

- user表
储存基本信息和bp1-100的bid

- beatmap表
储存用户在谱面上的最好记录