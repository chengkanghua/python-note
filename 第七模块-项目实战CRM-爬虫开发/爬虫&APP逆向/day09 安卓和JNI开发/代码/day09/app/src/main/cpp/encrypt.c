/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
/* Header for class com_nb_day09_encryptUtils */

#ifndef _Included_com_nb_day09_encryptUtils
#define _Included_com_nb_day09_encryptUtils
#ifdef __cplusplus
extern "C" {
#endif
/*
 * Class:     com_nb_day09_encryptUtils
 * Method:    add
 * Signature: (II)I
 */
JNIEXPORT jint JNICALL
Java_com_nb_day09_encryptUtils_add(JNIEnv *env, jclass obj, jint v1, jint v2) {
    // 写C语言代码 + env是JNI对象 + obj当前类encryptUtils + 参数
    return v1 + v2;
}

/*
 * Class:     com_nb_day09_encryptUtils
 * Method:    sign
 * Signature: (Ljava/lang/String;)Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL
Java_com_nb_day09_encryptUtils_sign(JNIEnv *env, jclass obj, jstring origin) {
    // C语言生成字符串
    char data[] = "wupeiqi";
    return (*env)->NewStringUTF(env, data);
}

#ifdef __cplusplus
}
#endif
#endif
