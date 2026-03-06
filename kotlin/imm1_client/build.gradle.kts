plugins {
    kotlin("js") version "2.0.21"
}

group = "online.itvia.svperitus"
version = "0.1.0"

repositories {
    mavenCentral()
}

kotlin {
    js(IR) {
        browser {
            binaries.executable()
        }
    }

    sourceSets {
        val main by getting {
            dependencies {
            }
        }
        val test by getting {
            dependencies {
            }
        }
    }
}
