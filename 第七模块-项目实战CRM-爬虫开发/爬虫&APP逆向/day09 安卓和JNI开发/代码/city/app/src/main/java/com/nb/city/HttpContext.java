package com.nb.city;

class HttpContext {
    public int code;
    public String message;

    public HttpContext(int code, String msg) {
        this.code = code;
        this.message = msg;
    }
}
