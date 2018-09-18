var { execSync } = require('child_process');

var escapeShell = function(cmd) {
  return '"'+cmd.replace(/(["\s'$`\\])/g,'\\$1')+'"';
};

const url = process.argv[2];

const script = `\"var script = document.createElement('script');\
script.setAttribute('src','${url}');\
document.head.appendChild(script);\"`;

const tabId = execSync(`./chrome-cli info`).toString().split('\n')[0].split(': ')[1];
execSync(`./chrome-cli execute ${script} -t ${tabId}`);
