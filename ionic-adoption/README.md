Optional, use something like [nvm](https://github.com/nvm-sh/nvm) to manage node installs. I tested with Node v18.17.0.

Install ionic: `npm install -g @ionic/cli`

Set the value in `src/constants.ts` to the API's base address. I haven't thought of a better way to do this yet. I may introduce a variable to differentiate dev and production builds? I need to research more how to do this. Since the app is distributed to a mobile device, I don't think this is a great place for using an environment variable. I also don't think it's likely there is a lot of variation between dev environments for this value.

For local testing use: `ionic serve`

Open with browser and use dev tools to get an approximation of what the app will look like on an Android device.

---------

To build for Android, install Android Studio.Then set the environment variable CAPACITOR_ANDROID_STUDIO_PATH to Android Studio's location (e.g. /usr/local/android-studio/bin/studio.sh).

Add Android platform to the project: `ionic cap add android`

Build web version with `ionic build` and sync the Android version with `ionic cap sync`

It should be possible for build for iOS as well, but I do not have a Mac to test this with.