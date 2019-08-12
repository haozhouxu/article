# sharepoint学习笔记

## SharePoint的版本（2019-8-12）
- 通过下面的地址，可以获取到文件的信息和当前的版本号，Doclib8...是一个文件夹的相对路径
```
http://sev-sp/sites/main/_api/Web/GetFolderByServerRelativeUrl('/sites/main/DocLib8....')/Files
```

- 通过下面的地址，可以获取到文件的历史版本信息和文件下载地址，DocLib8....是一个文件的相对路径
```
http://sev-sp/sites/main/_api/Web/GetFileByServerRelativeUrl('/sites/main/DocLib8....')/Versions
```
