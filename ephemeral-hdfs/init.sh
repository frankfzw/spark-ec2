#!/bin/bash

pushd /home/ubuntu > /dev/null

if [ -d "ephemeral-hdfs" ]; then
  echo "Ephemeral HDFS seems to be installed. Exiting."
  return 0
fi

case "$HADOOP_MAJOR_VERSION" in
  1)
    wget http://s3.amazonaws.com/spark-related-packages/hadoop-1.0.4.tar.gz
    echo "Unpacking Hadoop"
    tar xvzf hadoop-1.0.4.tar.gz > /tmp/spark-ec2_hadoop.log
    rm hadoop-*.tar.gz
    mv hadoop-1.0.4/ ephemeral-hdfs/
    sed -i 's/-jvm server/-server/g' /home/ubuntu/ephemeral-hdfs/bin/hadoop
    cp /home/ubuntu/hadoop-native/* /home/ubuntu/ephemeral-hdfs/lib/native/
    ;;
  2) 
    wget http://s3.amazonaws.com/spark-related-packages/hadoop-2.0.0-cdh4.2.0.tar.gz  
    echo "Unpacking Hadoop"
    tar xvzf hadoop-*.tar.gz > /tmp/spark-ec2_hadoop.log
    rm hadoop-*.tar.gz
    mv hadoop-2.0.0-cdh4.2.0/ ephemeral-hdfs/

    # Have single conf dir
    rm -rf /home/ubuntu/ephemeral-hdfs/etc/hadoop/
    ln -s /home/ubuntu/ephemeral-hdfs/conf /home/ubuntu/ephemeral-hdfs/etc/hadoop
    cp /home/ubuntu/hadoop-native/* /home/ubuntu/ephemeral-hdfs/lib/native/
    ;;
  yarn)
    wget http://s3.amazonaws.com/spark-related-packages/hadoop-2.4.0.tar.gz
    echo "Unpacking Hadoop"
    tar xvzf hadoop-*.tar.gz > /tmp/spark-ec2_hadoop.log
    rm hadoop-*.tar.gz
    mv hadoop-2.4.0/ ephemeral-hdfs/

    # Have single conf dir
    rm -rf /home/ubuntu/ephemeral-hdfs/etc/hadoop/
    ln -s /home/ubuntu/ephemeral-hdfs/conf /home/ubuntu/ephemeral-hdfs/etc/hadoop
    ;;

  *)
     echo "ERROR: Unknown Hadoop version"
     return 1
esac
/home/ubuntu/spark-ec2/copy-dir /home/ubuntu/ephemeral-hdfs

popd > /dev/null
