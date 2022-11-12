package com.nb.city;

import java.util.ArrayList;

class Item {
    public int id;
    public String name;

    @Override
    public String toString() {
        return "Item{" +
                "id=" + id +
                ", name='" + name + '\'' +
                '}';
    }
}

class HttpResponse {
    public String url;
    public String token;
    public ArrayList<Item> dataList;

    @Override
    public String toString() {
        return "HttpResponse{" +
                "url='" + url + '\'' +
                ", token='" + token + '\'' +
                ", dataList=" + dataList +
                '}';
    }
}

