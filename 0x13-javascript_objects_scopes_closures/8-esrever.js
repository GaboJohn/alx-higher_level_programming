#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let y = 0;
  while ((len - y) > 0) {
    const aux = list[len];
    list[len] = list[y];
    list[y] = aux;
    y++;
    len--;
  }
  return list;
};
