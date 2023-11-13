# ai_exercise

## one 2D image to multi 2d image
3D_model/another_angle_2ディレクトリで実行できる。app.pyをstreamlitで実行すると、
簡易的なGUIアプリケーションが立ち上がる。このアプリではdiffusionモデルによって生成された, 複数枚の別アングルの写真を取捨選別して入手することができる。

## Structure from Motion
3D_model/OpenSfMディレクトリでOpenSfMを実行することができる。自身の写真で実行するには、
適切に写真をセットしなければいけない。dockerfileをdocker(linux)上で実行すれば実行できる。

## 3D matching
OpenPCDetをビルドし、KITTIデータセットをダウンロードする。
data_processフォルダの内容で前処理を行い、training_KITTI_DDP.pyにて学習する。
KITTI以外の場合は自分で実装する必要がある。学習とテストも同一プログラム内である。
