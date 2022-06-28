import execjs

javascript_file = execjs.compile('''
function createGUID() {
    var e = (new Date).getTime().toString(36)
      , t = Math.random().toString(36).replace(/^0./, "");
    return "".concat(e, "_").concat(t)
}
''')

guid = javascript_file.call('createGUID')
print(guid)
pid = javascript_file.call('createGUID')
print(pid)
flowid = pid + "_" + "4330701"
print(flowid)
